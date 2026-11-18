// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("alert-triage")
export class BuildDecision {
  @Post("buildDecision")
  async buildDecision(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    let grievance;
    try { grievance = JSON.parse(summary).value || summary; }
    catch (e) { grievance = summary; }
    JSON.parse(grievance);
    return { created: true };
  }
}
