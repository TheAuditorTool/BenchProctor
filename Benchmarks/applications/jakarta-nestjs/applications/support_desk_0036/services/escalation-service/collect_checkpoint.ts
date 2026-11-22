// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("escalation-service")
export class CollectCheckpoint {
  @Post("collectCheckpoint")
  async collectCheckpoint(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["x-custom-header"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(preface);
    const grievance: string = readInput();
    const reportSpec = jsYaml.load(String(grievance), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
