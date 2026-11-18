const express = require("express");
const session = require("express-session");

const applyWatermark = require("./watermark_apply").applyWatermark;
const annotateReceipt = require("./annotate_receipt").annotateReceipt;
const normalizeCaption = require("./normalize_caption").normalizeCaption;
const compactManifest = require("./compact_manifest").compactManifest;
const enrichReport = require("./enrich_report").enrichReport;
const archiveConfig = require("./archive_config").archiveConfig;
const annotateManifest = require("./annotate_manifest").annotateManifest;
const publishReport = require("./publish_report").publishReport;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/applyWatermark", route(applyWatermark));
app.post("/annotateReceipt", route(annotateReceipt));
app.post("/normalizeCaption", route(normalizeCaption));
app.post("/compactManifest", route(compactManifest));
app.post("/enrichReport", route(enrichReport));
app.post("/archiveConfig", route(archiveConfig));
app.post("/annotateManifest", route(annotateManifest));
app.post("/publishReport", route(publishReport));

app.listen(3000, "0.0.0.0");
