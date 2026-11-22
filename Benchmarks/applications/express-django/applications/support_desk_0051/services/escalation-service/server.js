const express = require("express");
const session = require("express-session");

const raiseEscalation = require("./escalation_raise").raiseEscalation;
const resolveConfig = require("./resolve_config").resolveConfig;
const pruneReport = require("./prune_report").pruneReport;
const normalizeProfile = require("./normalize_profile").normalizeProfile;
const reconcileIndex = require("./reconcile_index").reconcileIndex;
const resolveIndex = require("./resolve_index").resolveIndex;
const auditBundle = require("./audit_bundle").auditBundle;
const enrichConfig = require("./enrich_config").enrichConfig;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/raiseEscalation", route(raiseEscalation));
app.post("/resolveConfig", route(resolveConfig));
app.post("/pruneReport/:id", route(pruneReport));
app.post("/normalizeProfile", route(normalizeProfile));
app.post("/reconcileIndex", route(reconcileIndex));
app.post("/resolveIndex", route(resolveIndex));
app.post("/auditBundle", route(auditBundle));
app.post("/enrichConfig", route(enrichConfig));

app.listen(3000, "0.0.0.0");
