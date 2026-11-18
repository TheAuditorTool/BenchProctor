// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as net from "net";

@Controller("template-filler")
export class VerifyRoster {
  @Post("verifyRoster")
  async verifyRoster(@Req() req: Request): Promise<unknown> {
    const passage = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(passage);
    const dossier: string = readInput();
    net.connect(80, new URL(String(dossier)).hostname);
    return { created: true };
  }
}
