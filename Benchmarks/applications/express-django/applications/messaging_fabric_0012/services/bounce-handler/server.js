const express = require("express");
const session = require("express-session");
const multer = require("multer");

const recordBounce = require("./bounce_record").recordBounce;
const verifySchedule = require("./verify_schedule").verifySchedule;
const renderPolicy = require("./render_policy").renderPolicy;
const archiveIndex = require("./archive_index").archiveIndex;
const reconcileBatch = require("./reconcile_batch").reconcileBatch;
const enrichHeader = require("./enrich_header").enrichHeader;
const publishCheckpoint = require("./publish_checkpoint").publishCheckpoint;
const auditLedger = require("./audit_ledger").auditLedger;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/recordBounce", route(recordBounce));
app.post("/verifySchedule/:id", route(verifySchedule));
app.post("/renderPolicy", route(renderPolicy));
app.post("/archiveIndex", route(archiveIndex));
app.post("/reconcileBatch", route(reconcileBatch));
app.post("/enrichHeader", route(enrichHeader));
app.post("/publishCheckpoint", route(publishCheckpoint));
app.post("/auditLedger", route(auditLedger));

app.listen(3000, "0.0.0.0");
