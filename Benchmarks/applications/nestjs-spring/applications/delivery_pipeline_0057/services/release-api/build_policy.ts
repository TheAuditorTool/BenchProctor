// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as net from "net";

@Controller("release-api")
export class BuildPolicy {
  @Post("buildPolicy")
  async buildPolicy(@Req() req: Request): Promise<unknown> {
    const footnote = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(footnote);
    const wording: string = readInput();
    net.connect(80, new URL(String(wording)).hostname);
    return { created: true };
  }
}
