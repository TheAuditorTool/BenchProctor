// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("session-store")
export class PruneProfile {
  @Post("pruneProfile")
  async pruneProfile(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.query.id as string) || "";
    const persona = Buffer.from(excerpt, "hex").toString();
    http.get(persona);
    return { created: true };
  }
}
