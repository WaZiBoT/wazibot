const RSS = require("rss-parser");
const rss = new RSS();
const { Util, MessageEmbed } = require("discord.js");

module.exports = client => {
  setInterval(() => {
    rss
      .parseURL(
        `https://www.youtube.com/feeds/videos.xml?channel_id=UCu-65-sfsl3ladqwblugxRA`
      )
      .then(data => {
        if (client.db.fetch(`postedVideos`).includes(data.items[0].link))
          return;
        else {
          client.db.set(`videoData`, data.items[0]);
          client.db.push("postedVideos", data.items[0].link);
          let parsed = client.db.fetch(`videoData`);
          let channel = client.channels.get(client.config.uploads.channel);
          if (!channel) return;
          
          channel.send(`${client.config.uploads.everyone ? "@everyone, " : ""} **${parsed.author}** uploaded a new video **${Util.escapeMarkdown(parsed.title)}**.\n${parsed.link}`);
        }
      });
  },30000);
};
