import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { schedulePublication } from "./publish_schedule";
import { resolveSchedule } from "./resolve_schedule";
import { normalizeCheckpoint } from "./normalize_checkpoint";
import { publishReport } from "./publish_report";
import { normalizePolicy } from "./normalize_policy";
import { publishSnapshot } from "./publish_snapshot";
import { fetchReceipt } from "./fetch_receipt";
import { reconcileArticle } from "./reconcile_article";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/schedulePublication", schedulePublication);
app.post("/resolveSchedule", resolveSchedule);
app.post("/normalizeCheckpoint", normalizeCheckpoint);
app.post("/publishReport", publishReport);
app.post("/normalizePolicy", normalizePolicy);
app.post("/publishSnapshot", publishSnapshot);
app.post("/fetchReceipt", fetchReceipt);
app.post("/reconcileArticle", reconcileArticle);

app.listen(3000, "0.0.0.0");
