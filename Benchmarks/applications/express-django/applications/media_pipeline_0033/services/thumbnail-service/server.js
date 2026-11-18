const express = require("express");
const session = require("express-session");

const renderThumbnail = require("./thumbnail_render").renderThumbnail;
const collectManifest = require("./collect_manifest").collectManifest;
const collectConfig = require("./collect_config").collectConfig;
const normalizeReport = require("./normalize_report").normalizeReport;
const enrichReport = require("./enrich_report").enrichReport;
const renderSnapshot = require("./render_snapshot").renderSnapshot;
const loadLedger = require("./load_ledger").loadLedger;
const pruneSnapshot = require("./prune_snapshot").pruneSnapshot;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/renderThumbnail", route(renderThumbnail));
app.post("/collectManifest", route(collectManifest));
app.post("/collectConfig", route(collectConfig));
app.post("/normalizeReport", route(normalizeReport));
app.post("/enrichReport", route(enrichReport));
app.post("/renderSnapshot", route(renderSnapshot));
app.post("/loadLedger", route(loadLedger));
app.post("/pruneSnapshot", route(pruneSnapshot));

app.listen(3000, "0.0.0.0");
