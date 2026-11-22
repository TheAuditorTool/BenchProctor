const express = require("express");
const session = require("express-session");
const multer = require("multer");

const runCycleCount = require("./cycle_count").runCycleCount;
const summarizeHeader = require("./summarize_header").summarizeHeader;
const auditStock = require("./audit_stock").auditStock;
const annotateSnapshot = require("./annotate_snapshot").annotateSnapshot;
const annotateSchedule = require("./annotate_schedule").annotateSchedule;
const buildSnapshot = require("./build_snapshot").buildSnapshot;
const enrichLedger = require("./enrich_ledger").enrichLedger;
const archiveLedger = require("./archive_ledger").archiveLedger;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/runCycleCount", route(runCycleCount));
app.post("/summarizeHeader", route(summarizeHeader));
app.post("/auditStock", route(auditStock));
app.post("/annotateSnapshot", route(annotateSnapshot));
app.post("/annotateSchedule", route(annotateSchedule));
app.post("/buildSnapshot", route(buildSnapshot));
app.post("/enrichLedger", route(enrichLedger));
app.post("/archiveLedger", route(archiveLedger));

app.listen(3000, "0.0.0.0");
