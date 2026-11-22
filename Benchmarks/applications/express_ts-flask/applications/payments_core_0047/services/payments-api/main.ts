import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { authorizePayment } from "./payment_authorize";
import { annotateSnapshot } from "./annotate_snapshot";
import { auditReport } from "./audit_report";
import { buildPayout } from "./build_payout";
import { fetchRecord } from "./fetch_record";
import { reconcileDispute } from "./reconcile_dispute";
import { fetchProfile } from "./fetch_profile";
import { buildDispute } from "./build_dispute";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/authorizePayment", authorizePayment);
app.post("/annotateSnapshot", annotateSnapshot);
app.post("/auditReport/:id", auditReport);
app.post("/buildPayout", buildPayout);
app.post("/fetchRecord", fetchRecord);
app.post("/reconcileDispute", reconcileDispute);
app.post("/fetchProfile", fetchProfile);
app.post("/buildDispute", buildDispute);

app.listen(3000, "0.0.0.0");
