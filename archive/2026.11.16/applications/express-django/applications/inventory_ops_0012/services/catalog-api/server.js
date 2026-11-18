const express = require("express");
const session = require("express-session");

const lookupSku = require("./sku_lookup").lookupSku;
const buildReport = require("./build_report").buildReport;
const annotateAllocation = require("./annotate_allocation").annotateAllocation;
const reconcileConfig = require("./reconcile_config").reconcileConfig;
const formatManifest = require("./format_manifest").formatManifest;
const renderReport = require("./render_report").renderReport;
const summarizeSummary = require("./summarize_summary").summarizeSummary;
const summarizeBatch = require("./summarize_batch").summarizeBatch;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/lookupSku", route(lookupSku));
app.post("/buildReport", route(buildReport));
app.post("/annotateAllocation", route(annotateAllocation));
app.post("/reconcileConfig", route(reconcileConfig));
app.post("/formatManifest", route(formatManifest));
app.post("/renderReport", route(renderReport));
app.post("/summarizeSummary", route(summarizeSummary));
app.post("/summarizeBatch", route(summarizeBatch));

app.listen(3000, "0.0.0.0");
