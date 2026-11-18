const express = require("express");
const session = require("express-session");

const cutRelease = require("./release_cut").cutRelease;
const buildPolicy = require("./build_policy").buildPolicy;
const archiveReport = require("./archive_report").archiveReport;
const rotateLedger = require("./rotate_ledger").rotateLedger;
const publishCheckpoint = require("./publish_checkpoint").publishCheckpoint;
const compactReport = require("./compact_report").compactReport;
const publishProfile = require("./publish_profile").publishProfile;
const rotateBundle = require("./rotate_bundle").rotateBundle;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/cutRelease", route(cutRelease));
app.post("/buildPolicy", route(buildPolicy));
app.post("/archiveReport", route(archiveReport));
app.post("/rotateLedger", route(rotateLedger));
app.post("/publishCheckpoint", route(publishCheckpoint));
app.post("/compactReport", route(compactReport));
app.post("/publishProfile", route(publishProfile));
app.post("/rotateBundle", route(rotateBundle));

app.listen(3000, "0.0.0.0");
