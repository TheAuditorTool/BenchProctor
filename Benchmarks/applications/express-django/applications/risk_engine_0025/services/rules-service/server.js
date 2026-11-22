const express = require("express");
const session = require("express-session");

const evaluateRule = require("./rule_evaluate").evaluateRule;
const verifyCheckpoint = require("./verify_checkpoint").verifyCheckpoint;
const formatDigest = require("./format_digest").formatDigest;
const pruneSnapshot = require("./prune_snapshot").pruneSnapshot;
const archiveRoster = require("./archive_roster").archiveRoster;
const buildCase = require("./build_case").buildCase;
const fetchRoster = require("./fetch_roster").fetchRoster;
const archiveReceipt = require("./archive_receipt").archiveReceipt;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/evaluateRule", evaluateRule);
app.post("/verifyCheckpoint", verifyCheckpoint);
app.post("/formatDigest", formatDigest);
app.post("/pruneSnapshot", pruneSnapshot);
app.post("/archiveRoster", archiveRoster);
app.post("/buildCase", buildCase);
app.post("/fetchRoster", fetchRoster);
app.post("/archiveReceipt", archiveReceipt);

app.listen(3000, "0.0.0.0");
