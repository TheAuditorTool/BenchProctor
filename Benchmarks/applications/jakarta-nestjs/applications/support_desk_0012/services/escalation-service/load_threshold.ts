// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("escalation-service")
export class LoadThreshold {
  @Post("loadThreshold")
  async loadThreshold(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const grievance: string = transform(summary);
    return "<div>" + grievance + "</div>";
  }
}
