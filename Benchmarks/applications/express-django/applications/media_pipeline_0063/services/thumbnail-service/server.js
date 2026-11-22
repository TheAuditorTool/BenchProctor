const express = require("express");
const session = require("express-session");
const multer = require("multer");

const renderThumbnail = require("./thumbnail_render").renderThumbnail;
const pruneManifest = require("./prune_manifest").pruneManifest;
const enrichThreshold = require("./enrich_threshold").enrichThreshold;
const publishConfig = require("./publish_config").publishConfig;
const annotateSchedule = require("./annotate_schedule").annotateSchedule;
const normalizeRecord = require("./normalize_record").normalizeRecord;
const enrichSnapshot = require("./enrich_snapshot").enrichSnapshot;
const pruneRecord = require("./prune_record").pruneRecord;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/renderThumbnail", renderThumbnail);
app.post("/pruneManifest", pruneManifest);
app.post("/enrichThreshold", enrichThreshold);
app.post("/publishConfig", publishConfig);
app.post("/annotateSchedule", annotateSchedule);
app.post("/normalizeRecord", normalizeRecord);
app.post("/enrichSnapshot", enrichSnapshot);
app.post("/pruneRecord", pruneRecord);

app.listen(3000, "0.0.0.0");
