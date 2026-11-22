// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("audit-log")
export class AppendAudit {
  @Post("appendAudit")
  async appendAudit(@Req() req: Request): Promise<unknown> {
    const heading = req.body.platform_payload || "";
    http.get(heading);
    return { created: true };
  }
}
