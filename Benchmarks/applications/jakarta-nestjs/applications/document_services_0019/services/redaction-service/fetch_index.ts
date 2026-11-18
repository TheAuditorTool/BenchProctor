// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("redaction-service")
export class FetchIndex {
  @Post("fetchIndex")
  async fetchIndex(@Req() req: Request): Promise<unknown> {
    const passage = (req.query.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(passage);
    const dossier: string = readInput();
    JSON.parse(dossier);
    return { created: true };
  }
}
