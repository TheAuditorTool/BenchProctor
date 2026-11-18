// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("payments-api")
export class MergeBatch {
  @Post("mergeBatch")
  async mergeBatch(@Req() req: Request): Promise<unknown> {
    const caption = (req.query.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(caption);
    const ledger: string = readInput();
    JSON.parse(ledger);
    return { created: true };
  }
}
