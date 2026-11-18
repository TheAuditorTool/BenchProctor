// SPDX-License-Identifier: Apache-2.0
import { Controller, Param, Post } from "@nestjs/common";
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
  @Post("BenchmarkTest00443/:id")
  async BenchmarkTest00443(@Param("id") pathId: string): Promise<unknown> {
    const userInput = pathId;
    const transform = (v: string): string => v.trim();
    const data: string = transform(userInput);
    childProcess.execSync("echo " + data);
    return { created: true };
  }
}
