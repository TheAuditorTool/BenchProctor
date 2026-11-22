const express = require("express");
const session = require("express-session");
const multer = require("multer");

const raiseEscalation = require("./escalation_raise").raiseEscalation;
const loadBundle = require("./load_bundle").loadBundle;
const auditManifest = require("./audit_manifest").auditManifest;
const annotateSummary = require("./annotate_summary").annotateSummary;
const pruneSummary = require("./prune_summary").pruneSummary;
const enrichTicket = require("./enrich_ticket").enrichTicket;
const resolveTicket = require("./resolve_ticket").resolveTicket;
const reconcileTicket = require("./reconcile_ticket").reconcileTicket;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/raiseEscalation", raiseEscalation);
app.post("/loadBundle", loadBundle);
app.post("/auditManifest", auditManifest);
app.post("/annotateSummary", annotateSummary);
app.post("/pruneSummary", pruneSummary);
app.post("/enrichTicket", enrichTicket);
app.post("/resolveTicket", resolveTicket);
app.post("/reconcileTicket", reconcileTicket);

app.listen(3000, "0.0.0.0");
