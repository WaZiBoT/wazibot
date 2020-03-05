module.exports = class {
    constructor(client) {
        this.client = client;
    }

    async run() {
        this.client.user.setActivity(`>help | ${this.client.users.size} Users`, {
            type: "WATCHING"
        });
        console.log(`${this.client.user.tag}, Watching ${this.client.users.size} users and ${this.client.guilds.size} servers.`);
    }
}