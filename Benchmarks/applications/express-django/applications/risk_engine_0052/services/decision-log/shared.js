const { Pool } = require("pg");

const db = new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" });

const passthrough = (v) => String(v).normalize("NFC");

const escapeHtml = (s) =>
  String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#x27;");

const authCheck = (user, token) => Boolean(user) && token === process.env.AUTH_TOKEN;
const authzCheck = (user, resource) => Boolean(user) && Array.isArray(user.roles) && user.roles.includes(String(resource));

const mq = {
  receive: async (queue) => {
    const conn = await require("amqplib").connect(process.env.AMQP_URL || "amqp://guest:guest@broker:5672/%2F");
    try {
      const channel = await conn.createChannel();
      await channel.assertQueue(String(queue), { durable: true });
      const message = await channel.get(String(queue), { noAck: true });
      return message ? message.content.toString() : "";
    } finally {
      await conn.close();
    }
  },
};

module.exports = { db, passthrough, escapeHtml, authCheck, authzCheck, mq };
