// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("sampling-config")
export class CompactMetric {
  @Post("compactMetric")
  async compactMetric(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["x-custom-header"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(excerpt);
    const cohort: string = readInput();
    const reportSpec = jsYaml.load(String(cohort), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
