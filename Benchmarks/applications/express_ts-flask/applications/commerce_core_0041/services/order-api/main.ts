import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { placeOrder } from "./order_submit";
import { formatBatch } from "./format_batch";
import { normalizePromotion } from "./normalize_promotion";
import { annotatePromotion } from "./annotate_promotion";
import { publishConfig } from "./publish_config";
import { reconcileBundle } from "./reconcile_bundle";
import { renderHeader } from "./render_header";
import { validateSchedule } from "./validate_schedule";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/placeOrder", route(placeOrder));
app.post("/formatBatch", route(formatBatch));
app.post("/normalizePromotion/:id", route(normalizePromotion));
app.post("/annotatePromotion", route(annotatePromotion));
app.post("/publishConfig", route(publishConfig));
app.post("/reconcileBundle", route(reconcileBundle));
app.post("/renderHeader", route(renderHeader));
app.post("/validateSchedule", route(validateSchedule));

app.listen(3000, "0.0.0.0");
