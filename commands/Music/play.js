const Command = require("../../Base/Command");
const YouTube = require("simple-youtube-api");
const youtube = new YouTube(process.env.YOUTUBE);

class Play extends Command {
  constructor(client) {
    super(client, {
      name: "play",
      aliases: ["p"],
      usage: ["play <songname>", "play <songURL>", "play <song-id>"],
      description: "Plays a song."
    });
  }

  async run(message, args, Discord) {
    const query = args.join(" ");
    const url = args[0] ? args[0].replace(/<(.+)>/g, "$1") : "";
    if (!message.member.voice.channel)
      return message.channel.send(
        "❌ | Can you try again by joining voice channel?"
      );
    if (!query)
      return message.channel.send(
        "❌ | Can you try again by providing search query?"
      );
    if (
      !message.member.voice.channel
        .permissionsFor(this.client.user)
        .has("CONNECT")
    )
      return message.channel.send(
        "❌ | Ahoy, looks like I can't join your voice channel!"
      );
    if (
      !message.member.voice.channel
        .permissionsFor(this.client.user)
        .has("SPEAK")
    )
      return message.channel.send(
        "❌ | Ahoy, looks like I can't speak on your voice channel!"
      );
    const voiceChannel = message.member.voice.channel;
    if (!message.guild.me.voice.channel)
      await message.member.voice.channel.join();
    if (voiceChannel && message.guild.me.voice.channel.id !== voiceChannel.id)
      return message.channel.send(`❌ | You are not in my voice channel!`);
    const playing = this.client.queue.get(message.guild.id);
    if (playing && playing.songs.length >= 20) return message.channel.send("❌ | Can't queue more songs, please try again later!");
    if (url.match(/^https?:\/\/(www.youtube.com|youtube.com)\/playlist(.*)$/)) {
      message.channel.send("🔍 Searching playlist `" + query + "`").then(msg => {
      msg.delete(1000);
    });
      const playlist = await youtube.getPlaylist(url);
      const videos = await playlist.getVideos();
      let video2;
      for (const video of Object.values(videos)) {
        if (youtube.getVideoByID(video.id)) {
          video2 = await youtube.getVideoByID(video.id);
          await this.client.player.handleVideo(
            video2,
            message,
            voiceChannel,
            true
          );
        } else return;
      }
      return;
    } else {
      try {
        var video = await youtube.getVideo(url);
      } catch (error) {
        try {
          var videos = await youtube.searchVideos(query, 3);
          let index = 0;
          message.channel.send("🔍 Searching query `" + query + "`").then(msg => {
            msg.delete(1000);
          });
          var video = await youtube.getVideoByID(videos[0].id);
        } catch (err) {
          return message.channel.send("❌ | Too many requests. Please try again later!");
        }
      }
      return this.client.player.handleVideo(video, message, voiceChannel);
    }
  }
}

module.exports = Play;
