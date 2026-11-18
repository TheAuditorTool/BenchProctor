// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("config-service")
export class RenderQuota {
  @Post("renderQuota")
  async renderQuota(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.referer as string) || "";
    const handshake = excerpt != null ? excerpt : '';
    const fileContent = fs.readFileSync("/var/app/data/" + handshake, "utf8");
    return fileContent;
  }
}
