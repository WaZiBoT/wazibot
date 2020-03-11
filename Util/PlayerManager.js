const Discord = require("discord.js");
const ytdl = require("discord-ytdl-core");

class PlayerManager {
  /**
   * @constructor
   * @param {Client} client Discord Client
   */
  constructor(client) {
    this.client = client;
  }

  /**
   * handleVideo
   * @param {Video} video vdo
   * @param {Message} message msg
   * @param {voiceChannel} voiceChannel vc
   * @param {Playlist} [playlist=false] boolean
   */
  async handleVideo(video, message, voiceChannel, playlist = false) {
    const serverQueue = this.client.queue.get(message.guild.id);
    const song = {
      id: video.id,
      title: Discord.Util.escapeMarkdown(video.title),
      url: `https://www.youtube.com/watch?v=${video.id}`,
      channel: {
        title: video.channel.title,
        id: video.channel.id,
        url: `https://youtube.com/channel/${video.channel.id}`
      },
      duration: video.duration,
      duration2:
        video.duration.hours * 3.6e6 +
        video.duration.minutes * 60000 +
        video.duration.seconds * 1000,
      requestedBy: message.author,
      requestedAt: new Date(),
      requestedTimestamp: Date.now()
    };
    if (!serverQueue) {
      const queueConstruct = {
        textChannel: message.channel,
        voiceChannel: voiceChannel,
        connection: null,
        songs: [],
        volume: 5,
        playing: true,
        loop: false,
        gain: 0,
        bold: false
      };
      this.client.queue.set(message.guild.id, queueConstruct);

      queueConstruct.songs.push(song);

      try {
        var connection = await voiceChannel.join();
        queueConstruct.connection = connection;
        await this.play(message.guild, queueConstruct.songs[0]);
      } catch (error) {
        console.error(error);
        this.client.queue.delete(message.guild.id);
        return message.channel.send(
          `😡 | Error came up while playing the song. Please try again later.`
        );
      }
    } else {
      serverQueue.songs.push(song);
      if (playlist) return;
      else {
        const embed = new Discord.MessageEmbed()
          .setAuthor("Song Queued!", message.guild.iconURL({ dynamic: true }))
          .setColor("#7289DA")
          .setDescription(`**[${song.title}](${song.url})**`)
          .setFooter(
            `Requested by: ${song.requestedBy.tag}`,
            song.requestedBy.displayAvatarURL({ dynamic: true })
          )
          .setTimestamp()
          .setThumbnail(
            `https://img.youtube.com/vi/${song.id}/maxresdefault.jpg`
          )
          .addField(
            `Channel`,
            `**[${song.channel.title}](https://youtube.com/channel/${song.channel.id})**`,
            true
          )
          .addField(
            `Duration`,
            `\`${song.duration.hours}:${song.duration.minutes}:${song.duration.seconds}\``,
            true
          );
        message.channel.send(embed).catch(e => {});
      }
    }
    return;
  }

  /**
   * play
   * @param {guild} guild guild
   * @param {song} song song
   */
  async play(guild, song) {
    const serverQueue = this.client.queue.get(guild.id);
    if (!guild.me.voice.channel) {
      this.client.queue.delete(guild.id);
      return serverQueue.textChannel.send("Music player has ended!");
    }
    if (!song) {
      this.client.queue.delete(guild.id);
      serverQueue.voiceChannel.leave();
      return serverQueue.textChannel.send("Music player has ended!");
    }
    const outputStream = ytdl(song.url, {
      filter: "audioonly",
      highWaterMark: 1024 * 1024 * 10,
      encoderArgs: ["-af", serverQueue.pitchdown && serverQueue.gain < 1 ? `asetrate=44100*0.9,aresample=44100,atempo=1.1` : `equalizer=f=40:width_type=h:width=50:g=${serverQueue.gain}`]
    });
    const dispatcher = serverQueue.connection
      .play(outputStream, {
        type: "opus",
        highWaterMark: 1,
        volume: serverQueue.volume / 100
      })
      .on("end", reason => {
        if (serverQueue.loop === true)
          serverQueue.songs.push(serverQueue.songs.shift());
        else serverQueue.songs.shift();
        this.play(guild, serverQueue.songs[0]);
      })
      .on("error", error => console.error(error));
    dispatcher.setVolumeLogarithmic(serverQueue.volume / 5);
    serverQueue.dispatcher = dispatcher;

    const embed = new Discord.MessageEmbed()
      .setAuthor("Started Playing", guild.iconURL({ dynamic: true }))
      .setThumbnail(`https://img.youtube.com/vi/${song.id}/maxresdefault.jpg`)
      .addField(`Song`, `**[${song.title}](${song.url})**`)
      .addField(
        `Channel`,
        `**[${song.channel.title}](${song.channel.url})**`,
        true
      )
      .addField(
        `Duration`,
        `\`${song.duration.hours}:${song.duration.minutes}:${song.duration.seconds}\``,
        true
      )
      .setColor("#7289DA")
      .setFooter(
        `Requested by: ${song.requestedBy.tag}`,
        song.requestedBy.displayAvatarURL({ dynamic: true })
      )
      .setTimestamp(song.requestedAt);
    return serverQueue.textChannel.send(embed).catch(e => {});
  }

  /**
   * createBar
   * @param {shifted} shifted time
   * @param {total} total time
   */
  createBar(shifted, total) {
    let indicator = "🔘";
    let index = Math.round((shifted / total) * 15);
    if (index >= 1 && index <= 15) {
      let bar = `▬▬▬▬▬▬▬▬▬▬▬▬▬▬`.split("");
      bar.insert(index, indicator);
      return bar.join("");
    } else {
      return `${indicator}▬▬▬▬▬▬▬▬▬▬▬▬▬▬`;
    }
  }
}

module.exports = PlayerManager;
