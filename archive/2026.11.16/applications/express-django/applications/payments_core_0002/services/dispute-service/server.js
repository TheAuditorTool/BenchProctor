const express = require("express");
const session = require("express-session");

const openDispute = require("./dispute_open").openDispute;
const rotateMandate = require("./rotate_mandate").rotateMandate;
const resolveIndex = require("./resolve_index").resolveIndex;
const enrichWallet = require("./enrich_wallet").enrichWallet;
const auditReport = require("./audit_report").auditReport;
const mergeIndex = require("./merge_index").mergeIndex;
const compactCheckpoint = require("./compact_checkpoint").compactCheckpoint;
const archiveProfile = require("./archive_profile").archiveProfile;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/openDispute", route(openDispute));
app.post("/rotateMandate", route(rotateMandate));
app.post("/resolveIndex", route(resolveIndex));
app.post("/enrichWallet", route(enrichWallet));
app.post("/auditReport", route(auditReport));
app.post("/mergeIndex", route(mergeIndex));
app.post("/compactCheckpoint", route(compactCheckpoint));
app.post("/archiveProfile", route(archiveProfile));

app.listen(3000, "0.0.0.0");
