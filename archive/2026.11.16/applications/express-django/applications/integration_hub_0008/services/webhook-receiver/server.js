const express = require("express");
const session = require("express-session");

const acceptWebhook = require("./webhook_accept").acceptWebhook;
const reconcileBatch = require("./reconcile_batch").reconcileBatch;
const enrichLedger = require("./enrich_ledger").enrichLedger;
const auditRoster = require("./audit_roster").auditRoster;
const verifyPartner = require("./verify_partner").verifyPartner;
const enrichWebhook = require("./enrich_webhook").enrichWebhook;
const reconcileSchedule = require("./reconcile_schedule").reconcileSchedule;
const publishThreshold = require("./publish_threshold").publishThreshold;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/acceptWebhook", route(acceptWebhook));
app.post("/reconcileBatch", route(reconcileBatch));
app.post("/enrichLedger", route(enrichLedger));
app.post("/auditRoster", route(auditRoster));
app.post("/verifyPartner", route(verifyPartner));
app.post("/enrichWebhook", route(enrichWebhook));
app.post("/reconcileSchedule", route(reconcileSchedule));
app.post("/publishThreshold", route(publishThreshold));

app.listen(3000, "0.0.0.0");
