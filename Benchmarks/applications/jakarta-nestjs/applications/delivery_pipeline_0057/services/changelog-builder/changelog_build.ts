// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("changelog-builder")
export class BuildChangelog {
  @Post("buildChangelog")
  async buildChangelog(@Req() req: Request): Promise<unknown> {
    const tagline = req.body.delivery_payload || "";
    http.get(tagline);
    return { created: true };
  }
}
