const express = require("express");
const session = require("express-session");

const ingestMetric = require("./metric_ingest").ingestMetric;
const archiveReceipt = require("./archive_receipt").archiveReceipt;
const reconcileSample = require("./reconcile_sample").reconcileSample;
const mergeReport = require("./merge_report").mergeReport;
const reconcileSchedule = require("./reconcile_schedule").reconcileSchedule;
const resolveWindow = require("./resolve_window").resolveWindow;
const rotateDigest = require("./rotate_digest").rotateDigest;
const mergeReceipt = require("./merge_receipt").mergeReceipt;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/ingestMetric", route(ingestMetric));
app.post("/archiveReceipt", route(archiveReceipt));
app.post("/reconcileSample", route(reconcileSample));
app.post("/mergeReport", route(mergeReport));
app.post("/reconcileSchedule", route(reconcileSchedule));
app.post("/resolveWindow", route(resolveWindow));
app.post("/rotateDigest", route(rotateDigest));
app.post("/mergeReceipt", route(mergeReceipt));

app.listen(3000, "0.0.0.0");
