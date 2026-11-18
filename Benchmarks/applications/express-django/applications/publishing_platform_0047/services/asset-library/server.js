const express = require("express");
const session = require("express-session");

const attachAsset = require("./asset_attach").attachAsset;
const reconcileRecord = require("./reconcile_record").reconcileRecord;
const archiveSchedule = require("./archive_schedule").archiveSchedule;
const resolveCheckpoint = require("./resolve_checkpoint").resolveCheckpoint;
const fetchRoster = require("./fetch_roster").fetchRoster;
const formatManifest = require("./format_manifest").formatManifest;
const validateBundle = require("./validate_bundle").validateBundle;
const compactRecord = require("./compact_record").compactRecord;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/attachAsset/:id", route(attachAsset));
app.post("/reconcileRecord", route(reconcileRecord));
app.post("/archiveSchedule", route(archiveSchedule));
app.post("/resolveCheckpoint", route(resolveCheckpoint));
app.post("/fetchRoster", route(fetchRoster));
app.post("/formatManifest", route(formatManifest));
app.post("/validateBundle", route(validateBundle));
app.post("/compactRecord/:id", route(compactRecord));

app.listen(3000, "0.0.0.0");
