const express = require("express");
const session = require("express-session");

const startCheckout = require("./checkout_session").startCheckout;
const publishSchedule = require("./publish_schedule").publishSchedule;
const compactThreshold = require("./compact_threshold").compactThreshold;
const summarizeLedger = require("./summarize_ledger").summarizeLedger;
const summarizeSchedule = require("./summarize_schedule").summarizeSchedule;
const exportSchedule = require("./export_schedule").exportSchedule;
const exportDigest = require("./export_digest").exportDigest;
const fetchPromotion = require("./fetch_promotion").fetchPromotion;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/startCheckout", route(startCheckout));
app.post("/publishSchedule", route(publishSchedule));
app.post("/compactThreshold", route(compactThreshold));
app.post("/summarizeLedger", route(summarizeLedger));
app.post("/summarizeSchedule", route(summarizeSchedule));
app.post("/exportSchedule", route(exportSchedule));
app.post("/exportDigest", route(exportDigest));
app.post("/fetchPromotion", route(fetchPromotion));

app.listen(3000, "0.0.0.0");
