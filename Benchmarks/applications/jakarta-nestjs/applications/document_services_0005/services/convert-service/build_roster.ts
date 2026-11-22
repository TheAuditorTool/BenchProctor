// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("convert-service")
export class BuildRoster {
  @Post("buildRoster")
  async buildRoster(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["user-agent"] as string) || "";
    http.get(footnote);
    return { created: true };
  }
}
