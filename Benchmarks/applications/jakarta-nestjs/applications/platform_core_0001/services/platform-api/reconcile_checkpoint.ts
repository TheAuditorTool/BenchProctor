// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("platform-api")
export class ReconcileCheckpoint {
  @Post("reconcileCheckpoint")
  async reconcileCheckpoint(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers["user-agent"] as string) || "";
    http.get(tagline);
    return { created: true };
  }
}
