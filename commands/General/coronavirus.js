const Command = require("../../Base/Command");

class Covid extends Command {
  constructor(client) {
    super(client, {
      name: "coronavirus",
      description: "Get information about coronavirus",
      usage: ["coronavirus"],
      aliases: ["covid", "covid19"]
    });
  }

  async run(message, args, Discord) {
    if (args[0]) {
      this.client
        .request("https://corona.lmao.ninja/countries")
        .then(res => res.json())
        .then(body => {
          const mapping = body.filter(
            c => c.country.toLowerCase() === args[0].toLowerCase()
          );
          if (mapping.length < 1) return message.reply("not found");
          mapping.map(map => {
            let embed = new Discord.MessageEmbed()
              .setColor("#FF0000")
              .setAuthor(
                "Coronavirus Stats",
                "https://images.newscientist.com/wp-content/uploads/2020/01/27123401/f0070229-coronavirus_artwork-spl.jpg"
              )
              .setThumbnail(
                "https://images.newscientist.com/wp-content/uploads/2020/01/27123401/f0070229-coronavirus_artwork-spl.jpg"
              )
              .setTitle(map.country)
              .addField("Total Cases:", map.cases.toLocaleString(), true)
              .addField("Deaths:", map.deaths.toLocaleString(), true)
              .addField("Recovered:", map.recovered.toLocaleString(), true)
              .addField("Active:", map.active.toLocaleString(), true)
              .addField("Deaths Today:", map.todayDeaths.toLocaleString(), true)
              .addField("Cases Today:", map.todayCases.toLocaleString(), true)
              .addField("Critical:", map.critical.toLocaleString(), true)
              .addField(
                "Cases Per Million:",
                map.casesPerOneMillion.toLocaleString()
              , true)
              .setTimestamp();
            return message.channel.send(embed);
          });
        });
    } else {
      this.client
        .request("https://corona.lmao.ninja/all")
        .then(res => res.json())
        .then(body => {
          const embed = new Discord.MessageEmbed()
            .setColor("#FF0000")
            .setAuthor(
              "Coronavirus Stats",
              "https://images.newscientist.com/wp-content/uploads/2020/01/27123401/f0070229-coronavirus_artwork-spl.jpg"
            )
            .setThumbnail(
              "https://images.newscientist.com/wp-content/uploads/2020/01/27123401/f0070229-coronavirus_artwork-spl.jpg"
            )
            .addField("Total Cases:", body.cases.toLocaleString())
            .addField("Deaths:", body.deaths.toLocaleString())
            .addField("Recovered:", body.recovered.toLocaleString())
            .setFooter("Last Update:")
            .setTimestamp(body.updated);
          return message.channel.send(embed);
        });
    }
  }
}

module.exports = Covid;
