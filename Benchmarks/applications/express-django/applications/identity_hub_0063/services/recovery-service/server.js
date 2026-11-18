const express = require("express");
const session = require("express-session");

const startRecovery = require("./recovery_start").startRecovery;
const summarizeBundle = require("./summarize_bundle").summarizeBundle;
const mergeThreshold = require("./merge_threshold").mergeThreshold;
const resolveBatch = require("./resolve_batch").resolveBatch;
const reconcileConfig = require("./reconcile_config").reconcileConfig;
const publishConfig = require("./publish_config").publishConfig;
const renderReport = require("./render_report").renderReport;
const exportHeader = require("./export_header").exportHeader;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/startRecovery", route(startRecovery));
app.post("/summarizeBundle", route(summarizeBundle));
app.post("/mergeThreshold", route(mergeThreshold));
app.post("/resolveBatch", route(resolveBatch));
app.post("/reconcileConfig", route(reconcileConfig));
app.post("/publishConfig", route(publishConfig));
app.post("/renderReport", route(renderReport));
app.post("/exportHeader", route(exportHeader));

app.listen(3000, "0.0.0.0");
