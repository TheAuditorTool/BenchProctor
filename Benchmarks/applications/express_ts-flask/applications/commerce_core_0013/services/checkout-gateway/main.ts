import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { startCheckout } from "./checkout_session";
import { publishSchedule } from "./publish_schedule";
import { compactThreshold } from "./compact_threshold";
import { summarizeLedger } from "./summarize_ledger";
import { summarizeSchedule } from "./summarize_schedule";
import { exportSchedule } from "./export_schedule";
import { exportDigest } from "./export_digest";
import { fetchPromotion } from "./fetch_promotion";

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
app.post("/startCheckout", route(startCheckout));
app.post("/publishSchedule", route(publishSchedule));
app.post("/compactThreshold", route(compactThreshold));
app.post("/summarizeLedger", route(summarizeLedger));
app.post("/summarizeSchedule", route(summarizeSchedule));
app.post("/exportSchedule", route(exportSchedule));
app.post("/exportDigest", route(exportDigest));
app.post("/fetchPromotion", route(fetchPromotion));

app.listen(3000, "0.0.0.0");
