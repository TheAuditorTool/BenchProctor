const express = require("express");
const session = require("express-session");

const routeTicket = require("./ticket_route").routeTicket;
const enrichMacro = require("./enrich_macro").enrichMacro;
const annotateLedger = require("./annotate_ledger").annotateLedger;
const resolveRoster = require("./resolve_roster").resolveRoster;
const auditSummary = require("./audit_summary").auditSummary;
const reconcileProfile = require("./reconcile_profile").reconcileProfile;
const archiveThreshold = require("./archive_threshold").archiveThreshold;
const buildLedger = require("./build_ledger").buildLedger;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/routeTicket", route(routeTicket));
app.post("/enrichMacro", route(enrichMacro));
app.post("/annotateLedger", route(annotateLedger));
app.post("/resolveRoster", route(resolveRoster));
app.post("/auditSummary", route(auditSummary));
app.post("/reconcileProfile", route(reconcileProfile));
app.post("/archiveThreshold", route(archiveThreshold));
app.post("/buildLedger", route(buildLedger));

app.listen(3000, "0.0.0.0");
