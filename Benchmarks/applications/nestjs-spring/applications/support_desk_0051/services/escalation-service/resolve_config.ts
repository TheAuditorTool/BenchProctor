// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("escalation-service")
export class ResolveConfig {
  @Post("resolveConfig")
  async resolveConfig(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["x-custom-header"] as string) || "";
    const _raw = preface;
    const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
    return "<div>" + grievance + "</div>";
  }
}
