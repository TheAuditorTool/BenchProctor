// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Query, ForbiddenException } from "@nestjs/common";
import { Response } from "express";
import * as fs from "fs";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00370")
  async BenchmarkTest00370(@Query("id") id: string): Promise<unknown> {
    const userInput = id || "";
    const data = userInput != null ? userInput : '';
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(data)) { throw new ForbiddenException({error:"forbidden"}); }
    const checkedPath = "/var/app/data/" + data;
    fs.writeFileSync(checkedPath, "data");
    return { created: true };
  }
}
