// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("reconcile-service")
export class ExportPayout {
  @Post("exportPayout")
  async exportPayout(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers["user-agent"] as string) || "";
    http.get(headline);
    return { created: true };
  }
}
