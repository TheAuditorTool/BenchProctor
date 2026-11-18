const express = require("express");
const session = require("express-session");

const configureSample = require("./sample_config").configureSample;
const pruneDigest = require("./prune_digest").pruneDigest;
const compactManifest = require("./compact_manifest").compactManifest;
const exportRoster = require("./export_roster").exportRoster;
const verifyThreshold = require("./verify_threshold").verifyThreshold;
const validateRecord = require("./validate_record").validateRecord;
const pruneCheckpoint = require("./prune_checkpoint").pruneCheckpoint;
const exportHeader = require("./export_header").exportHeader;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/configureSample", route(configureSample));
app.post("/pruneDigest", route(pruneDigest));
app.post("/compactManifest/:id", route(compactManifest));
app.post("/exportRoster", route(exportRoster));
app.post("/verifyThreshold", route(verifyThreshold));
app.post("/validateRecord", route(validateRecord));
app.post("/pruneCheckpoint", route(pruneCheckpoint));
app.post("/exportHeader", route(exportHeader));

app.listen(3000, "0.0.0.0");
