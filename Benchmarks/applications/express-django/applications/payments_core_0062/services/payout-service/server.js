const express = require("express");
const session = require("express-session");

const schedulePayout = require("./payout_schedule").schedulePayout;
const collectReport = require("./collect_report").collectReport;
const compactIndex = require("./compact_index").compactIndex;
const enrichDigest = require("./enrich_digest").enrichDigest;
const renderBatch = require("./render_batch").renderBatch;
const normalizeSnapshot = require("./normalize_snapshot").normalizeSnapshot;
const formatManifest = require("./format_manifest").formatManifest;
const buildIndex = require("./build_index").buildIndex;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/schedulePayout", route(schedulePayout));
app.post("/collectReport", route(collectReport));
app.post("/compactIndex", route(compactIndex));
app.post("/enrichDigest", route(enrichDigest));
app.post("/renderBatch", route(renderBatch));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/formatManifest", route(formatManifest));
app.post("/buildIndex", route(buildIndex));

app.listen(3000, "0.0.0.0");
