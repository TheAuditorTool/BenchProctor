const express = require("express");
const session = require("express-session");

const routeTicket = require("./ticket_route").routeTicket;
const reconcileCheckpoint = require("./reconcile_checkpoint").reconcileCheckpoint;
const pruneHeader = require("./prune_header").pruneHeader;
const enrichBundle = require("./enrich_bundle").enrichBundle;
const resolveSurvey = require("./resolve_survey").resolveSurvey;
const pruneSnapshot = require("./prune_snapshot").pruneSnapshot;
const validateBundle = require("./validate_bundle").validateBundle;
const pruneReceipt = require("./prune_receipt").pruneReceipt;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/routeTicket", route(routeTicket));
app.post("/reconcileCheckpoint/:id", route(reconcileCheckpoint));
app.post("/pruneHeader", route(pruneHeader));
app.post("/enrichBundle", route(enrichBundle));
app.post("/resolveSurvey", route(resolveSurvey));
app.post("/pruneSnapshot", route(pruneSnapshot));
app.post("/validateBundle", route(validateBundle));
app.post("/pruneReceipt", route(pruneReceipt));

app.listen(3000, "0.0.0.0");
