// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("convert-service")
export class RenderSnapshot {
  @Post("renderSnapshot")
  async renderSnapshot(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["user-agent"] as string) || "";
    http.get(preface);
    return { created: true };
  }
}
