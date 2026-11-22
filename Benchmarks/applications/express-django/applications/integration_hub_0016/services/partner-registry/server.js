const express = require("express");
const session = require("express-session");
const multer = require("multer");

const registerPartner = require("./partner_register").registerPartner;
const renderWebhook = require("./render_webhook").renderWebhook;
const pruneCheckpoint = require("./prune_checkpoint").pruneCheckpoint;
const rotateDigest = require("./rotate_digest").rotateDigest;
const compactPolicy = require("./compact_policy").compactPolicy;
const renderWindow = require("./render_window").renderWindow;
const loadSchedule = require("./load_schedule").loadSchedule;
const pruneBatch = require("./prune_batch").pruneBatch;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/registerPartner", route(registerPartner));
app.post("/renderWebhook", route(renderWebhook));
app.post("/pruneCheckpoint/:id", route(pruneCheckpoint));
app.post("/rotateDigest", route(rotateDigest));
app.post("/compactPolicy", route(compactPolicy));
app.post("/renderWindow", route(renderWindow));
app.post("/loadSchedule", route(loadSchedule));
app.post("/pruneBatch", route(pruneBatch));

app.listen(3000, "0.0.0.0");
