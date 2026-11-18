// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("article-api")
export class VerifyDigest {
  @Post("verifyDigest")
  async verifyDigest(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    const pending: string[] = String(summary).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const addendum: string = collected.join(',');
    net.connect(80, new URL(String(addendum)).hostname);
    return { created: true };
  }
}
