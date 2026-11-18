// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as childProcess from "child_process";
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
  @Post("BenchmarkTest00489")
  async BenchmarkTest00489(@Body("field") field: string): Promise<unknown> {
    const userInput = field || "";
    const transform = (v: string): string => v.trim();
    const data: string = transform(userInput);
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(data)) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    childProcess.execSync("echo " + processed);
    return { created: true };
  }
}
