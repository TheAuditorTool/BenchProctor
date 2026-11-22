import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { enrollDevice } from "./device_enroll";
import { summarizeIndex } from "./summarize_index";
import { annotateProfile } from "./annotate_profile";
import { summarizePolicy } from "./summarize_policy";
import { exportSummary } from "./export_summary";
import { reconcileSummary } from "./reconcile_summary";
import { renderSnapshot } from "./render_snapshot";
import { annotatePolicy } from "./annotate_policy";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/enrollDevice", route(enrollDevice));
app.post("/summarizeIndex", route(summarizeIndex));
app.post("/annotateProfile", route(annotateProfile));
app.post("/summarizePolicy/:id", route(summarizePolicy));
app.post("/exportSummary", route(exportSummary));
app.post("/reconcileSummary/:id", route(reconcileSummary));
app.post("/renderSnapshot", route(renderSnapshot));
app.post("/annotatePolicy", route(annotatePolicy));

app.listen(3000, "0.0.0.0");
