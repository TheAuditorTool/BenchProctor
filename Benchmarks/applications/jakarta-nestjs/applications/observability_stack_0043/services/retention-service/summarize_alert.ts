// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("retention-service")
export class SummarizeAlert {
  @Post("summarizeAlert")
  async summarizeAlert(@Req() req: Request): Promise<unknown> {
    const note = (req.body.payload as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(note);
    const gauge: string = readInput();
    nodeSerialize.unserialize(gauge);
    return { created: true };
  }
}
