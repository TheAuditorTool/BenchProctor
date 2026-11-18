// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("syndication-feed")
export class ExportConfig {
  @Post("exportConfig")
  async exportConfig(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers["user-agent"] as string) || "";
    http.get(synopsis);
    return { created: true };
  }
}
