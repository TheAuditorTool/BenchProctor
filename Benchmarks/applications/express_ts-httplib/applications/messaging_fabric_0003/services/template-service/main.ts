import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { composeTemplate } from "./template_compose";
import { renderProfile } from "./render_profile";
import { rotateDelivery } from "./rotate_delivery";
import { validateSchedule } from "./validate_schedule";
import { validatePolicy } from "./validate_policy";
import { validateMessage } from "./validate_message";
import { annotateSchedule } from "./annotate_schedule";
import { loadRecord } from "./load_record";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/composeTemplate", route(composeTemplate));
app.post("/renderProfile", route(renderProfile));
app.post("/rotateDelivery/:id", route(rotateDelivery));
app.post("/validateSchedule", route(validateSchedule));
app.post("/validatePolicy", route(validatePolicy));
app.post("/validateMessage", route(validateMessage));
app.post("/annotateSchedule", route(annotateSchedule));
app.post("/loadRecord", route(loadRecord));

app.listen(3000, "0.0.0.0");
